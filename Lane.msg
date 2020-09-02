# This message contains the information of a lane (center line).
# It can be provided by the map, or produced by the fuser.

# The absolute index of the lane, which should be consistent with the map.
int64 id

# Relation of the lane to the vehicle.
int32 NEAR=1
int32 LEAD_TO=2
int32 relation

