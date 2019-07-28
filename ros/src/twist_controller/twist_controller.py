
GAS_DENSITY = 2.858
ONE_MPH = 0.44704


class Controller(object):
    def __init__(self, *args, **kwargs):
        #Controllers
        yaw_param = {}
        for key in ["wheel_base", "steer_ratio", "min_speed", "max_lat_accel", "max_steer_angle"]:
            yaw_param[key] = kwargs[key]

        self.yaw_controller = YawController(**yaw_param)
        k = [x * 0.462 for x in [1, 0.08, 0.006]]  # PID coefficients
        output_range = [kwargs["decel_limit"], kwargs["accel_limit"]]
        pid_param = k + output_range
        self.throttle_controller = PID(*pid_param)

        # Low pass filters
        self.ts = 1. / (kwargs["DBW_FREQ"])  # Sampling period
        self.tau = 2 * self.ts  # Cutoff frequency
        self.vel_lpf = LowPassFilter(self.tau, self.ts)

        # Vehicle parameters
        self.vehicle_mass = kwargs["vehicle_mass"]
        self.fuel_capacity = kwargs["fuel_capacity"]
        self.brake_deadband = kwargs["brake_deadband"]
        self.decel_limit = kwargs["decel_limit"]
        self.accel_limit = kwargs["accel_limit"]
        self.wheel_radius = kwargs["wheel_radius"]
        self.min_speed = kwargs["min_speed"]

        # Timestamp
        self.last_time = rospy.get_time()
        pass

    def control(self, *args, **kwargs):
        # TODO: Change the arg, kwarg list to suit your needs
        # Return throttle, brake, steer
        return 1., 0., 0.
