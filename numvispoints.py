{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3dc425b0",
   "metadata": {},
   "source": [
    "https://leetcode.com/problems/maximum-number-of-visible-points/"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a37dd44",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Solution: def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:\n",
    "    \n",
    "    if len(points)==1:\n",
    "        return 1\n",
    "\n",
    "    from math import pi, atan\n",
    "\n",
    "    # выражение угла в радианах\n",
    "    angle = angle*pi/180\n",
    "\n",
    "    # нормализация всех точек\n",
    "    i, j = location[0], location[1]\n",
    "    for k in range(len(points)):\n",
    "        x, y = points[k]\n",
    "        points[k] = [x-i, y-j]\n",
    "\n",
    "    # выражение всех точек в радианах\n",
    "    temp = []\n",
    "    for k in range(len(points)):\n",
    "        x, y = points[k]\n",
    "        if x!=0 or y!=0:\n",
    "            if x>0:\n",
    "                if y>=0:\n",
    "                    temp.append(atan(y/x))\n",
    "                else:\n",
    "                    temp.append(2*pi+atan(y/x))\n",
    "            elif x==0:\n",
    "                if y>0:\n",
    "                    temp.append(pi/2)\n",
    "                else:\n",
    "                    temp.append(3*pi/2)\n",
    "            elif x<0:\n",
    "                temp.append(pi+atan(y/x))\n",
    "\n",
    "    temp.sort()\n",
    "    \n",
    "    duplicate = []\n",
    "    for k in range(len(temp)):\n",
    "        duplicate.append(temp[k]+2*pi)\n",
    "    temp.extend(duplicate)\n",
    "\n",
    "    maxnum = 0\n",
    "    i, j = 0, 0\n",
    "    while j<len(temp):\n",
    "        if temp[j]-temp[i] <= angle:\n",
    "            maxnum = max(maxnum, j-i+1)\n",
    "            j+=1\n",
    "        else:\n",
    "            if i==j:\n",
    "                j+=1\n",
    "            else:\n",
    "                i+=1\n",
    "\n",
    "    return maxnum + points.count([0,0])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
