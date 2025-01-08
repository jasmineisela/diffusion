import math
from Diffusion import calculate_time_step

GRID_SPACING = 1.0
DIFFUSIVITY = 1.0
TIME = 0.5
TOLERANCE = 0.01

def test_time_step():
    time_step = calculate_time_step(GRID_SPACING, DIFFUSIVITY)
    assert type(time_step) is float 
    assert math.isclose(time_step, TIME, rel_tol=TOLERANCE)
    

