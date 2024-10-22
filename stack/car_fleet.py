"""
Car Fleet
There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car
and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same
speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the
destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.

Example 1:

Input: target = 10, position = [1,4], speed = [3,2]

Output: 1
Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet,
meeting each other at 10, the destination.

Example 2:

Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

Output: 3
Explanation: The cars starting at 4 and 7 become a fleet at position 10. The
cars starting at 1 and 0 never catch up to the car ahead of them. Thus, there
are 3 car fleets that will arrive at the destination.

Constraints:

n == position.length == speed.length.
1 <= n <= 1000
0 < target <= 1000
0 < speed[i] <= 100
0 <= position[i] < target
All the values of position are unique.

"""
def count_car_fleets(target, position, speed):
    # Combine position and speed and sort them
    pairs = sorted([[p, s] for p, s in zip(position, speed)])
    fleets = []

    for pair in pairs[::-1]:

        fleets.append(pair)

        if len(fleets) >= 2:
            # Because adding to stack in desc order,
            # top item in stack is at lower pos (behind) next-to-last one
            head_car_pos, head_car_speed = fleets[-2]
            head_car_time_to_dest = (target - head_car_pos) / head_car_speed

            tail_car_pos, tail_car_speed = fleets[-1]
            tail_car_time_to_dest = (target - tail_car_pos) / tail_car_speed

            # If head car takes longer to get to dest,
            # cars will collide & become a fleet
            if head_car_time_to_dest >= tail_car_time_to_dest:
                # So get rid of one of the cars
                fleets.pop()

    return len(fleets)

def test_count_car_fleets_two_cars_become_one_fleet():
    target = 10
    position = [1,4]
    speed = [3,2]

    expected = 1
    solution = count_car_fleets(target, position, speed)

    assert solution == expected

def test_count_car_fleets_four_cars_become_three_fleets():

    target = 10
    position = [4,1,0,7]
    speed = [2,2,1,1]

    expected = 3
    solution = count_car_fleets(target, position, speed)

    assert solution == expected
