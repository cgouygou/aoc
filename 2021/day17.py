#target area: x=96..125, y=-144..-98

class Target():
    def __init__(self, xmin, xmax, ymin, ymax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def within(self, probe):
        return probe.x in range(self.xmin, self.xmax+1) and probe.y in range(self.ymin, self.ymax+1)

    def is_reaching(self, velocity):
        p = Probe(0, 0, velocity)
        hmax = 0
        reached = False
        while p.x <= self.xmax and p.y >= self.ymin:
            p.actualise()
            hmax = max(hmax, p.y)
            if self.within(p):
                reached = True
        return reached, hmax

class Probe():
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.velocity = v

    def actualise(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.velocity = [max(0, self.velocity[0]-1), self.velocity[1]-1]

def find_xv_start(xmin):
    n = int(((2*(xmin -1))**0.5))
    while n*(n+1)//2 <= xmin:
        n += 1
    return n

target_area = Target(96, 125, -144, -98)
# target_area = Target(20, 30, -10, -5)

## Part 1
# y_max = 0
# for x  in range(find_xv_start(target_area.xmin), find_xv_start(target_area.xmax)):
#     for y in range(300):
#         if target_area.is_reaching((x, y))[0]:
#             y_max = max(y_max, target_area.is_reaching((x, y))[1])
#             velocity_max = (x, y)
#             # y += 1
#
# print(y_max)

## Part 2
velocities = []

for x  in range(find_xv_start(target_area.xmin), target_area.xmax+1):
    for y in range(300):
        if target_area.is_reaching((x, y+target_area.ymin))[0]:
            velocities.append((x, y+target_area.ymin))

print(len(velocities))

