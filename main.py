def define_env(env):
    @env.macro
    def supportMe():
        return '\n'.join([
            "!!! note \"Too Lazy?\"",
            "    Support me from as low as $5 a month and get the Ansible playbook for this manual among others, with a patron exclusive discord 😲"
        ])
