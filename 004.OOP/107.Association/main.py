# Association
from association import Pen, TypeWriter, Write

writer = Write('Joãozinho')
pen = Pen('Bic')
typewriter = TypeWriter()


writer.tool = typewriter
writer.tool.write()

del writer
print(Pen.brand)
typewriter.write()
