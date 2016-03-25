from pingdomexport.load import output_checks

def load(config, checks):
    # @todo use the config to understand what should be called
    output_checks.Output().process(checks)
