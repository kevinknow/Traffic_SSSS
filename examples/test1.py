from trafficSimulator import *

sim = Simulation()

lane_space = 3.5
intersection_size = 30
length = 70

# SOUTH, EAST, NORTH, WEST

# Intersection in
sim.create_segment((lane_space/2, length+intersection_size/2), (lane_space/2, intersection_size/2))
sim.create_segment((length+intersection_size/2, -lane_space/2), (intersection_size/2, -lane_space/2))
sim.create_segment((-lane_space/2, -length-intersection_size/2), (-lane_space/2, -intersection_size/2))
sim.create_segment((-length-intersection_size/2, lane_space/2), (-intersection_size/2, lane_space/2))


# Intersection out
sim.create_segment((-lane_space/2, intersection_size/2), (-lane_space/2, length+intersection_size/2))
sim.create_segment((intersection_size/2, lane_space/2), (length+intersection_size/2, lane_space/2))
sim.create_segment((lane_space/2, -intersection_size/2), (lane_space/2, -length-intersection_size/2))
sim.create_segment((-intersection_size/2, -lane_space/2), (-length-intersection_size/2, -lane_space/2))


# Straight
sim.create_segment((lane_space/2, intersection_size/2), (lane_space/2, -intersection_size/2))
sim.create_segment((intersection_size/2, -lane_space/2), (-intersection_size/2, -lane_space/2))
sim.create_segment((-lane_space/2, -intersection_size/2), (-lane_space/2, intersection_size/2))
sim.create_segment((-intersection_size/2, lane_space/2), (intersection_size/2, lane_space/2))


# Right turn
sim.create_quadratic_bezier_curve((lane_space/2, intersection_size/2), (lane_space/2, lane_space/2), (intersection_size/2, lane_space/2))
sim.create_quadratic_bezier_curve((intersection_size/2, -lane_space/2), (lane_space/2, -lane_space/2), (lane_space/2, -intersection_size/2))
sim.create_quadratic_bezier_curve((-lane_space/2, -intersection_size/2), (-lane_space/2, -lane_space/2), (-intersection_size/2, -lane_space/2))
sim.create_quadratic_bezier_curve((-intersection_size/2, lane_space/2), (-lane_space/2, lane_space/2), (-lane_space/2, intersection_size/2))

# Left turn
sim.create_quadratic_bezier_curve((lane_space/2, intersection_size/2), (lane_space/2, -lane_space/2), (-intersection_size/2, -lane_space/2))
sim.create_quadratic_bezier_curve((intersection_size/2, -lane_space/2), (-lane_space/2, -lane_space/2), (-lane_space/2, intersection_size/2))
sim.create_quadratic_bezier_curve((-lane_space/2, -intersection_size/2), (-lane_space/2, lane_space/2), (intersection_size/2, lane_space/2))
sim.create_quadratic_bezier_curve((-intersection_size/2, lane_space/2), (lane_space/2, lane_space/2), (lane_space/2, -intersection_size/2))





vg = VehicleGenerator({
    'vehicles': [
        (2, {'path': [0, 8, 6], 'v': 16.6}),
        (2, {'path': [0, 12, 5], 'v': 15.6}),
        (2, {'path': [0, 16, 7], 'v': 19.6})
        ]
    })
sim.add_vehicle_generator(vg)

# vg = VehicleGenerator({
#     'vehicles': [
#         (2, {'path': [0, 8, 6], 'v': 16.6}),
#         (2, {'path': [0, 12, 5], 'v': 15.6}),
#         (2, {'path': [0, 16, 7], 'v': 19.6})
#         ]
#     })
# sim.add_vehicle_generator(vg)

vg = VehicleGenerator({
    'vehicles': [
        (2, {'path': [0, 8, 6], 'v': 16.6}),
        (2, {'path': [0, 12, 5], 'v': 15.6}),
        (2, {'path': [0, 16, 7], 'v': 19.6})
        ]
    })
sim.add_vehicle_generator(vg)


vg = VehicleGenerator({                      
    'vehicles': [                               
       (2, {'path': [1, 9, 7], 'v': 10.6}),
        (2, {'path': [2, 14, 7], 'v': 13.6}),
        (2, {'path': [3, 15, 4], 'v': 13.6}),
        ]
    })
sim.add_vehicle_generator(vg)

vg = VehicleGenerator({
    'vehicles': [
       (2, {'path': [1, 9, 7], 'v': 10.6}),
        (2, {'path': [2, 14, 7], 'v': 13.6}),
        (2, {'path': [3, 15, 4], 'v': 13.6}),
        ]
    })
sim.add_vehicle_generator(vg)

vg = VehicleGenerator({
    'vehicles': [
       (2, {'path': [1, 13, 6], 'v': 17.6}),
       (2, {'path': [3, 11, 5], 'v': 16.6})       
    ]
    })
sim.add_vehicle_generator(vg)

# 13: 东转北     1，13，6             东向西  1，9，7 
# 14：北转西     2，14，7             西向东   3，11，5
# 15：西转南    3，15，4
# 16：南转西   0，16，7
# 18: 北转东    2，18，5
# 19：西转北   3，19， 6
# 17：东转南   1，17，4

# v = Vehicle({'path': [0], 'x': 20, 'v':16.6})
# sim.add_vehicle(v)

# v = Vehicle({'path': [0]})    # test code
# sim.add_vehicle(v)

win = Window(sim)
win.run()
win.show()
