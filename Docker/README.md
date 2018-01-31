Running the monkey from Docker
==============================
Build the chaos monkey first:
docker build -t monkey_chaos -f Dockerfile.chaos ../
docker build -t monkey_chaos32 -f Dockerfile.chaos32 ../

copy the files from the images to the dist dir in
the root of the project.

Build and run the island:
docker build -t monkey_island-f Dockerfile.island .
docker run --expose 5000 -p 5000:5000 monkey_island 

The simpliefied version is bash build.sh
