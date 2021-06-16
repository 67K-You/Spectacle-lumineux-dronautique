from pycrazyswarm import Crazyswarm
import uav_trajectory



def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf1 = swarm.allcfs.crazyflies[0]

    trajectory = uav_trajectory.Trajectory()
    trajectory.loadcsv('traj.csv')
    cf1.uploadTrajectory(1,0,trajectory)
    cf1.startTrajectory(1)

    timeHelper.sleep(39.0)



if __name__ == '__main__':
    main()
