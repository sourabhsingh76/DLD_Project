import src.base_module.module as module


class BlackBlock:
    module_name = 'BlackBlock'

    def __init__(self):
        pass

    def inputs(self):
        return ['G_i_k', 'P_i_k', 'G_km1_j', 'P_km1_j']

    def outputs(self):
        return ['G_i_j', 'P_i_j']

    def verilog(self, file_path, file_name):
        m = module.Module(BlackBlock.module_name)

        # Inputs
        for input in self.inputs():
            m.input(input, 'input')
        # Outputs
        for output in self.outputs():
            m.output(output, 'output')

        # Start
        m.start()

        # Assignments
        m.stmt_assign('G_i_j', 'G_i_k | ( P_i_k & G_km1_j )')
        m.stmt_assign('P_i_j', 'P_i_k & P_km1_j')

        # End
        m.end()

        # Write File
        m.write(file_path, file_name)

    @staticmethod
    def instantiation(instance_name, inputs, outputs):
        """
            inputs: [dict{ port: ? , connector: ?}]
            outputs: [dict{ port: ? , connector: ?}]
        """
        return module.Module.instantiate(module_name=BlackBlock.module_name,
                                         instance_name=instance_name,
                                         inputs=inputs,
                                         outputs=outputs)
