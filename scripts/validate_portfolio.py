"""Validate the local portfolio catalogue and installation references offline."""
from __future__ import annotations

import configparser
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tomllib


def validate(root: Path, check_git: bool = False) -> None:
    catalogue = json.loads((root / 'portfolio.json').read_text(encoding='utf-8'))
    pins = json.loads((root / 'source-pins.json').read_text(encoding='utf-8'))
    project = tomllib.loads((root / 'pyproject.toml').read_text(encoding='utf-8'))
    assert catalogue['schema_version'] == 1
    assert catalogue['hub'] == 'https://github.com/Ibekwemmanuel7/Lillie_US'
    products = {p['id']: p for p in catalogue['products']}
    assert len(products) == len(catalogue['products']) == 7
    assert set(products) == {'vhagar', 'vaughan', 'vulcan', 'vantage', 'vepris', 'viga', 'velo'}
    assert len({p['repository'] for p in products.values()}) == 7
    for p in products.values():
        assert p['repository'].startswith('https://github.com/Ibekwemmanuel7/')
        assert re.fullmatch(r'[0-9a-f]{40}', p['reference_commit']), p['id']
        assert p['domain'] and p['current_status']
        if p['source_commit'] is not None:
            assert re.fullmatch(r'[0-9a-f]{40}', p['source_commit']), p['id']
        else:
            assert p['integration'] == 'documentation-reference', p['id']
    dependencies = []
    for name, pin in pins['dependencies'].items():
        p = products[name]
        assert p['integration'] == 'python-dependency'
        assert p['source_commit'] == pin['commit']
        assert p['reference_commit'] == pin['documentation_commit']
        assert p['repository'] == pin['repository']
        dependencies.append(name + ' @ git+' + pin['repository'] + '@' + pin['commit'])
    assert sorted(dependencies) == sorted(project['project']['dependencies'])
    mineral = pins['components']['ml_mineral']
    assert mineral['commit'] == products['vulcan']['source_commit']
    assert mineral['repository'] == products['vulcan']['repository']
    assert mineral['path'] == 'modules/ml_mineral'
    modules = configparser.ConfigParser()
    modules.read(root / '.gitmodules', encoding='utf-8')
    assert modules.sections() == ['submodule "modules/ml_mineral"']
    assert modules[modules.sections()[0]]['url'] == mineral['repository']
    assert modules[modules.sections()[0]]['path'] == mineral['path']
    for name, pin in pins['planned_components'].items():
        p = products[name]
        assert p['source_commit'] is None
        assert pin['commit'] == p['reference_commit']
        assert pin['pin_scope'] == 'documentation-only'
        assert pin['repository'] == p['repository']
    for name in ['PORTFOLIO.md', 'REPOSITORY_STRATEGY.md', 'INTERFACES.md']:
        assert (root / 'docs' / name).is_file()
    readme = (root / 'README.md').read_text(encoding='utf-8')
    assert all(p['repository'].removesuffix('.git') in readme for p in products.values())
    if check_git:
        stage = subprocess.check_output(
            ['git', 'ls-files', '--stage', '--', mineral['path']], cwd=root, text=True
        ).split()
        assert len(stage) == 4 and stage[0] == '160000' and stage[1] == mineral['commit'] and stage[2] == '0'
        checkout = root / mineral['path']
        actual = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=checkout, text=True).strip()
        assert actual == mineral['commit']
        manifest = json.loads((checkout / 'SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
        for rel, record in manifest['files'].items():
            assert hashlib.sha256((checkout / rel).read_bytes()).hexdigest() == record['sha256'], rel
        tree = ''.join(k + '\0' + manifest['files'][k]['sha256'] + '\n' for k in sorted(manifest['files']))
        assert hashlib.sha256(tree.encode()).hexdigest() == manifest['tree_sha256']
    print('Portfolio valid: seven products; package pins, submodule configuration, documentation revisions and hub links agree.')


if __name__ == '__main__':
    validate(Path(__file__).resolve().parents[1], check_git='--check-git' in sys.argv)
