#String IO

import io

# Arbitrary String
message = 'This is just a normal string.'

f = io.StringIO(message)
print(f.read())
f.write(' Second line written to file like object')
#Reset cursor just like you would a file
f.seek(0)
print(f.read())
