"""River simulation using implemented Bear, Fish, and River classes."""

from river import River

my_river: River = River(50, 10)

my_river.view_river()

my_river.one_river_week()