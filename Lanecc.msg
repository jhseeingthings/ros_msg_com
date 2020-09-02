# This message contains the information of a lane (center line).
# It can be provided by the map, or produced by the fuser.

# The absolute index of the lane, which should be consistent with the map.
int64 id

# Relation of the lane to the vehicle.
int32 NEAR=1
int32 LEAD_TO=2
int32 relation

# Distance to the vehicle, with direction.
# This value is negative when the lane is on the left side of the vehicle, positive when right.
float32 offset

# Difference between the lane and the vehicle's heading, in rad.
# This value is negative when the lane is tilt to the left of the vehicle, positive when right.
float32 dirDiff

# Points on the lane, ordered according to the lane direction.
# In the relative coordinate system, "x" points to the front, "y" points to the left, "z" points upwards.
# In the absolute coordinate system, it should be consistent with the map.
geometry_msgs/Point32[] points

# If "relation=NEAR", this number is the index of the first point behind the vehicle, in the "points" array.
# If "relation=LEADTO", this number is useless.
int32 startPointIndex

# Direct distance to the next stop line.
geometry_msgs/Point32 nextStop

# Type of the stop line.
int32 NO_STOP=0
int32 SLOW_GIVE_WAY=1
int32 STOP_GIVE_WAY=2
int32 SEE_LIGHT=3
int32 LANE_END=4
int32 DESTINATION=5
int32 stopType

# Type of the traffic light
string lightType

# Where this lane leads to.
int64[] leadToIds

# Priority of this lane. Possible values are:
# 0 - Wrong lane;
# 1 - OK for now, but please change lane soon;
# 2 - Correct lane.
int32 preferred

# Indexes of the joint point corresponding to the "leadToIds".
int32[] jointIndexesInThisLane
int32[] jointIndexesInNextLane

# Id of the lane on the left.
int64 leftLaneId

# Id of the lane on the right.
int64 rightLaneId

# If you can make a lane change to the left.
bool canChangeLeft

# If you can make a lane change to the right.
bool canChangeRight

# A non-zero value of this variable represents that it is a reference path for turnning.
# For a non-zero value, the driver may need to look for traffic lights, and related turnning regulations.
int32 NONE=0
int32 STRAIGHT=1
int32 LEFT=2
int32 RIGHT=3
int32 UTURN=4
int32 turn

# The lower limit of speed.
# NOTICE: the unit is km/h, not m/s, please do necessary conversions.
float32 speedLowerLimit

# The upper limit of speed.
# NOTICE: the unit is km/h, not m/s, please do necessary conversions.
float32 speedUpperLimit

# The width of the lane.
float32 width
