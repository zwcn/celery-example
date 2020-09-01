from tasks.add import add
from tasks.minus import minus

add.delay(6, 6)

minus.delay(5, 5)
