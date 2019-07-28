from styx_msgs.msg import TrafficLight
import semaphoreDetection as SD

class TLClassifier(object):
    def __init__(self):
        # TODO load classifier
        # Not using classifier, so not needed

        pass

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """

        rospy.logdebug("tl_classifier: Classification requested")

        numRed, numGreen, numAmbar = SD.findSemaphore(image)

        if numRed > 1:
            rospy.logwarn("tl_classifier: RED light detected")
            return TrafficLight.RED

        elif numGreen > 1:
            rospy.logwarn("tl_classifier: GREEN light detected")
            return TrafficLight.GREEN

        elif numAmbar > 1:
            rospy.logwarn("tl_classifier: YELLOW light detected")
            return TrafficLight.YELLOW

        else:
            rospy.logwarn("tl_classifier: ERROR - UNKNOWN light")
            return TrafficLight.UNKNOWN

