#!/bin/sh
./gwu_cs_course_graph.py > graph.dot
dot -Tpng graph.dot > graph.png
