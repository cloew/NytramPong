from ..resources import ResourceDir

shaders = [Shader(1, ResourceDir.getProperPath("basic.vert"), ShaderTypes.VERTEX_SHADER),
           Shader(2, ResourceDir.getProperPath("basic.frag"), ShaderTypes.FRAGMENT_SHADER)]
shaderProgram = ShaderProgram(1, shaders)