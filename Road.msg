# This message tells the current road information.
# It also contains necessary data for navigation.

std_msgs/Header header

# An array that includes all lanes near the vehicle.
local_messages/Lane[] lanes

# Road type
int32 ROAD_NORMAL=1
int32 ROAD_UNSTRUCTED=2
int32 ROAD_PARKING=3
int32 type
