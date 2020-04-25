# Python math

Vac

```Python
# Current postion and velocity.
p[0] = p[0] + v[0]

# Position and velocity at the next time.
p[1] = p[1] + v[1]

```

## Point/point distance

* **Two points in math:**
  * p, q
* **Pythagorean theorem in math:**
  dist(p, q)<sup>2</sup> == (p[0] - q[0])<sup>2</sup> + (p[1] - q[1])<sup>2</sup>

```Python
# Two points in Python
# Python - The points are determined through a list of coordinates.
[p[0], p[1], [q[0], q[1]]]

# Pythagorean theorem in Python
def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)
```

## Vectors and motion

### Vector as difference of two points

* **Math - points on canvas:**
  * p,q
* **Math - Move/translate point using a vector:**
  p = q + v
* **Math - Updating for motion:**
  p = p + a * v

```Python
# Difference of two points
# Python - list of components
v[0] = p[0] - q[0]
v[1] = p[1] - q[1]

# Move/translate point using a vector.
# Python
p[0] = q[0] - v[0]
p[1] = q[1] - v[1]

# Updating for motion in Python
p[0] = q[0] + a * v[0]
p[1] = q[1] + a * v[1]
```

## Collisions

```Python
# Motion update
p[0] = q[0] + a * v[0]
p[1] = q[1] + a * v[1]

''' Collision of ball with center (p) and radius (r) with wall '''
# Left wall
p[0] <= r

# Right wall
p[0] >= width - r

# Top wall
p[1] <= r

# Bottom wall
p[1] >= height - r
```

## Reflections

```Python
# Motion update
p[0] = q[0] + a * v[0]
p[1] = q[1] + a * v[1]

# Reflections - update the velocity vector (v)

# Left wall - Compute reflected velocity vector
v[0] = -v[0]
v[1] = v[1]
```
