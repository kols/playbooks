from invoke import run, task

ROLES = [
    'workstations',
]
INVENTORIES = {}
PLAYBOOKS = {}

VIRTUALENV = 'ansible'
CMD = 'ansible-playbook'

for role in ROLES:
    INVENTORIES[role] = '%s.hosts' % role
    PLAYBOOKS[role] = '%s.yml' % role


def play(role, *opts):
    opts_str = ' '.join(opts)
    inventory = '-i {0}'.format(INVENTORIES[role])
    cmd = ' '.join([
        CMD,
        inventory,
        opts_str,
        PLAYBOOKS[role],
    ])
    run(cmd, pty=True)


@task
def play_local(host, role='workstations', sudo=True, opts=None):
    opts = opts and opts.split(' ') or []
    if sudo:
        opts.append('-K')
    opts.extend([
        '-c local',
        '-l {0}'.format(host),
    ])
    play(role, *opts)


@task
def play_remote():
    pass
