
## radial_blur (info)
***
Blurs the image by a certain amount outward from the center, as if the image is zooming in or out. As the distance from the center increases, the amount of blurring increases, and near the center the blur is hardly visible at all. The `size` value is smaller by default for this filter than it is for other filters, since it's typically used with an entire plane where the distance from the center can easily be several hundred pixels.

Typically this blur is used with an entire plane.

Note: Large blurs will look worse toward the edges due to limited sampling. Loss of accuracy will begin when `size` × distance is greather than 6. You can increase accuracy by breaking up large sizes into multiple filter passes. The blur used is Gaussian, so combining blur sizes A and B will give a total size of sqrt(A<sup>2</sup>+B<sup>2</sup>).

The `offset` parameter, if used, is effectively subtracted from the pixel distance to the center. Pixels within that radius won't blur. Anything outside that radius will act as if it's `offset` pixels closer to the center.
***