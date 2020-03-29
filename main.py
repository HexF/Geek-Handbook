def define_env(env):
    @env.macro
    def supportMe(manual):
        return '\n'.join([
            "!!! note",
            "    Support me from as low as $5 a month and get the Ansible playbook for `%s` along with many other playbooks" % (manual)
        ])
