from resources import ResourceDir
from nytram.shaders import Shader, ShaderProgram, ShaderTypes

shaders = [Shader(1, ResourceDir.getProperPath("basic.vert"), ShaderTypes.VERTEX_SHADER),
           Shader(2, ResourceDir.getProperPath("basic.frag"), ShaderTypes.FRAGMENT_SHADER)]
ShaderProgram = ShaderProgram(1, shaders)