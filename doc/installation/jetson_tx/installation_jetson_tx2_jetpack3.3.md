OpenPose - Installation on Nvidia Jetson TX2
====================================
Note that OpenPose for Nvidia Jetson TX2 was developed and it is maintained by the community. The OpenPose authors will not be able to provide official support for it.



## Contents
1. [Requirements and Dependencies](#requirements-and-dependencies)
2. [Installation](#installation)
3. [Usage](#usage)



## Requirements and Dependencies
Jetson TX2 just flashed with [JetPack 3.3](https://developer.nvidia.com/embedded/jetpack)

Notes:

- Installation is similar to Jetson TX1 and you can follow this [step by step tutorial](https://docs.nvidia.com/jetson/archives/jetpack-archived/jetpack-33/index.html#jetpack/3.3/install.htm%3FTocPath%3D_____3).
- If you are installing from a virtual machine host, installation may need to be done in two steps, please refer to [this solution](https://devtalk.nvidia.com/default/topic/1002081/jetson-tx2/jetpack-3-0-install-with-a-vm/).
- Be sure to complete both OS flashing and CUDA / cuDNN installation parts before installation.

**Dependencies**:

    - OpenCV (3.X versions are compatible).
    - Caffe and all its dependencies.
    - The demo and tutorials additionally use GFlags.



## Installation
Use the following script for installation of both caffe and OpenPose:
```
bash ./scripts/ubuntu/install_caffe_and_openpose_JetsonTX2_JetPack3.3.sh
```

Optional: If you want to build the Python libraries, then:
1. Edit the `BUILD_PYTHON` flag on `CMakeLists.txt`:

```option(BUILD_PYTHON "Build OpenPose python." ON)```

2. In both places where this appears, set the flag to ON:
```
-DBUILD_python=ON
-DBUILD_python_layer=ON
````

3. There are additional flags that need to be set: `PYTHON_EXECUTABLE=/usr/bin/python2.7` and `PYTHON_LIBRARY=/usr/lib/aarch64-linux-gnu/libpython2.7.so` for Python 2.7. Therefore, inside build, do:

```cmake -DBUILD_PYTHON=ON -DPYTHON_EXECUTABLE=/usr/bin/python2.7 -DPYTHON_LIBRARY=/usr/lib/aarch64-linux-gnu/libpython2.7.so ..```

4. Now run `make`.  You should see a file called "pyopenpose.so" if Python was set to 2.7, in
`/home/nvidia/openpose/build/python/openpose`. Otherwise, it will be `pyopenpose.cpython-35m-aarch64-linux-gnu`.

5. Finally, run `sudo make install` inside build to copy the files to /usr/local/python and set PYTHONPATH accordingly on .bashrc:

```export PYTHONPATH="${PYTHONPATH}:/usr/local/python```



## Usage
It is for now recommended to use an external camera with the demo. To get to decent FPS you need to lower the net resolution:
```
./build/examples/openpose/openpose.bin -camera_resolution 640x480 -net_resolution 128x96
```

To activate hand or face resolution please complete this command with the following options (warning, both simultaneously will cause out of memory error):
```
--hand -hand_net_resolution 256x256
--face -face_net_resolution 256x256
```
