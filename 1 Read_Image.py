{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2 as cv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "#read the image\n",
    "img = cv.imread(\"Ronaldo-1.jpg\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[196 193 202]\n",
      "  [200 196 201]\n",
      "  [202 197 199]\n",
      "  ...\n",
      "  [205 200 202]\n",
      "  [205 200 202]\n",
      "  [199 195 201]]\n",
      "\n",
      " [[201 198 200]\n",
      "  [204 200 199]\n",
      "  [206 201 198]\n",
      "  ...\n",
      "  [206 201 200]\n",
      "  [206 202 201]\n",
      "  [205 200 202]]\n",
      "\n",
      " [[201 195 200]\n",
      "  [204 199 198]\n",
      "  [204 199 198]\n",
      "  ...\n",
      "  [207 202 201]\n",
      "  [207 202 201]\n",
      "  [204 199 201]]\n",
      "\n",
      " ...\n",
      "\n",
      " [[211 201 201]\n",
      "  [208 203 202]\n",
      "  [207 203 202]\n",
      "  ...\n",
      "  [208 203 202]\n",
      "  [208 203 202]\n",
      "  [198 192 203]]\n",
      "\n",
      " [[212 201 203]\n",
      "  [208 202 203]\n",
      "  [209 204 203]\n",
      "  ...\n",
      "  [208 203 202]\n",
      "  [208 203 202]\n",
      "  [197 193 204]]\n",
      "\n",
      " [[209 198 201]\n",
      "  [206 199 202]\n",
      "  [206 199 202]\n",
      "  ...\n",
      "  [196 192 203]\n",
      "  [196 192 204]\n",
      "  [185 182 204]]]\n"
     ]
    }
   ],
   "source": [
    "#print array of image\n",
    "print(img)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Show the image\n",
    "cv.waitKey(delay = 5000)\n",
    "cv.destroyAllWindows()\n",
    "#show the image\n",
    "cv.imshow('image', img)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
