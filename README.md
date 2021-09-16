# PCVT - Point Cloud Visualization Tools

This project is established for visualizing point cloud data.

## pcvt1

pcvt1 create an image by matplotlib and visualize it with opencv. Also, you can save the image to file.

<img src="images/pcvt1.png">

## pcvt2

pcvt2 visualize point cloud with graphics library [Open3D](http://www.open3d.org/). It will create a window that you can rotate, scale and translate the point cloud with your mouse.

<img src="images/pcvt2_1.png" width="250px"><img src="images/pcvt2_2.png" width="250px"><img src="images/pcvt2_3.png" width="250px">

## pcvt3

pcvt3 visualize point cloud with matplotlib. The function `plot_pcd_one_view` can only visualize many point cloud in a fixed angle.

<img src="images/pcvt3_1.png">

The function `plot_pcd_three_views` will visualize every point cloud in three different views rotated along up axis. You also can add title for every point cloud.

<img src="images/pcvt3_2.png" width="400px">

You can reset the view angle and color by yourself.

## pcvt4

pcvt4 is cannot visualize the point cloud directly. It will create ball in every point of the point cloud and generate a mesh (`pc_mesh.ply`). In order to visualize the mesh, you can use the 3D modeling software such as [blender](https://www.blender.org/). For a sparse point cloud, you'd better set a larger radius.

Here are two examples visualized by blender:

<img src="images/pcvt4_1.png" width="400px">
<img src="images/pcvt4_2.png" width="400px">
