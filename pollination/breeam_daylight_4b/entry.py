from pollination_dsl.dag import Inputs, DAG, task, Outputs
from dataclasses import dataclass
from pollination.two_phase_daylight_coefficient import TwoPhaseDaylightCoefficientEntryPoint
from pollination.lbt_honeybee.postprocess import Breeam4b

# input/output alias
from pollination.alias.inputs.model import hbjson_model_grid_input
from pollination.alias.inputs.wea import wea_input_timestep_check
from pollination.alias.inputs.north import north_input
from pollination.alias.inputs.radiancepar import rad_par_annual_input
from pollination.alias.inputs.grid import grid_filter_input, \
    min_sensor_count_input, cpu_count


@dataclass
class BreeamDaylight4bEntryPoint(DAG):
    """BREEAM daylight 4b entry point."""

    # inputs
    north = Inputs.float(
        default=0,
        description='A number between -360 and 360 for the counterclockwise '
        'difference between the North and the positive Y-axis in degrees. This '
        'can also be a Vector for the direction to North. (Default: 0).',
        spec={'type': 'number', 'minimum': -360, 'maximum': 360},
        alias=north_input
    )

    cpu_count = Inputs.int(
        default=50,
        description='The maximum number of CPUs for parallel execution. This will be '
        'used to determine the number of sensors run by each worker.',
        spec={'type': 'integer', 'minimum': 1},
        alias=cpu_count
    )

    min_sensor_count = Inputs.int(
        description='The minimum number of sensors in each sensor grid after '
        'redistributing the sensors based on cpu_count. This value takes '
        'precedence over the cpu_count and can be used to ensure that '
        'the parallelization does not result in generating unnecessarily small '
        'sensor grids. The default value is set to 1, which means that the '
        'cpu_count is always respected.', default=500,
        spec={'type': 'integer', 'minimum': 1},
        alias=min_sensor_count_input
    )

    radiance_parameters = Inputs.str(
        description='The radiance parameters for ray tracing.',
        default='-ab 2 -ad 5000 -lw 2e-05 -dr 0',
        alias=rad_par_annual_input
    )

    grid_filter = Inputs.str(
        description='Text for a grid identifier or a pattern to filter the sensor grids '
        'of the model that are simulated. For instance, first_floor_* will simulate '
        'only the sensor grids that have an identifier that starts with '
        'first_floor_. By default, all grids in the model will be simulated.',
        default='*',
        alias=grid_filter_input
    )

    model = Inputs.file(
        description='A Honeybee Model JSON file (HBJSON) or a Model pkl (HBpkl) file. '
        'This can also be a zipped version of a Radiance folder, in which case this '
        'recipe will simply unzip the file and simulate it as-is.',
        extensions=['json', 'hbjson', 'pkl', 'hbpkl', 'zip'],
        alias=hbjson_model_grid_input
    )

    wea = Inputs.file(
        description='Wea file.',
        extensions=['wea', 'epw'],
        alias=wea_input_timestep_check
    )

    @task(
        template=TwoPhaseDaylightCoefficientEntryPoint
    )
    def run_two_phase_daylight_coefficient(
            self, north=north, cpu_count=cpu_count, min_sensor_count=min_sensor_count,
            radiance_parameters=radiance_parameters, grid_filter=grid_filter,
            model=model, wea=wea
    ):
        pass

    @task(
        template=Breeam4b,
        needs=[run_two_phase_daylight_coefficient]
    )
    def breem_daylight_4b(
        self, folder='results', model=model
    ):
        return [
            {
                'from': Breeam4b()._outputs.breeam_summary,
                'to': 'breeam_summary'
            }
        ]

    results = Outputs.folder(
        source='results', description='Folder with raw result files (.ill) that '
        'contain illuminance matrices for each sensor at each timestep of the analysis.'
    )

    breeam_summary = Outputs.folder(
        source='breeam_summary', description='BREEAM summary folder.'
    )

    summary = Outputs.file(
        description='JSON file containing the number of credits achieved.',
        source='breeam_summary/summary.json',
    )

    program_summary = Outputs.file(
        description='JSON file with a summary of each program type.',
        source='breeam_summary/program_summary.json',
    )
