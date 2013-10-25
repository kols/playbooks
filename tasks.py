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


@task
def play(role, sudo=True, *opts):
    opts = list(opts)
    if sudo:
        opts.append('-K')
    inv_opt = '-i %s' % INVENTORIES[role]
    cmd = ' '.join([CMD, inv_opt, ' '.join(opts), PLAYBOOKS[role]])
    run(cmd)


@task
def play_local(host, role='workstations'):
    opts = ['-c local', '-l {0}'.format(host),]
    play(role, True, *opts)
