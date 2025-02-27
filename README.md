# Starfield Simulation with Pygame

This project is a starfield simulation implemented using Pygame. It creates a 3D-like effect of stars moving toward the viewer, with rotating 6-pointed stars that change brightness as they approach. The stars are purple and retain their brightness properties, creating a visually appealing animation.

---

## Features

- **3D Starfield Effect**: Stars move toward the viewer, simulating depth using a Z-coordinate.
- **Rotating 6-Pointed Stars**: Each star is a rotating hexagram (6-pointed star).
- **Brightness Control**: Stars start dim and become brighter as they move closer.
- **Color Customization**: Stars are purple, and their brightness is applied dynamically.
- **Smooth Animation**: The simulation runs at 60 FPS for smooth motion.

---

## Design Choices

### 1. **Star Representation**
   - Each star is represented as a list `[x, y, z, brightness, rotation_angle]`:
     - `x`, `y`: 2D coordinates of the star.
     - `z`: Z-distance (depth) of the star.
     - `brightness`: Controls the star's brightness (0 to 255).
     - `rotation_angle`: Angle of rotation for the 6-pointed star.
   - **Justification**: Using a list is simple and efficient for storing star properties. Each property is easily accessible by index.

### 2. **Coordinate System**
   - The coordinate system is centered at the middle of the screen:
     - X and Y coordinates range from `-screen_width//2` to `+screen_width//2` and `-screen_hight//2` to `+screen_hight//2`.
   - **Justification**: Centering the coordinate system simplifies calculations for perspective and rotation.

### 3. **Perspective Calculation**
   - The on-screen position of each star is calculated using:
     \[
     x_{\text{screen}} = \frac{x \cdot 256}{z} + \text{screen\_center\_x}
     \]
     \[
     y_{\text{screen}} = \frac{y \cdot 256}{z} + \text{screen\_center\_y}
     \]
   - **Justification**: This formula simulates a 3D perspective effect, making stars appear smaller and slower as they move farther away.

### 4. **Brightness and Color**
   - The base color of the stars is purple `(128, 0, 128)`.
   - Brightness is applied dynamically by scaling the base color:
     \[
     \text{color} = \left(\frac{128 \cdot \text{brightness}}{255}, 0, \frac{128 \cdot \text{brightness}}{255}\right)
     \]
   - **Justification**: Separating brightness from color allows for smooth transitions and retains the star's visual properties.

### 5. **Rotation**
   - Each star rotates around its center using a `rotation_angle` property.
   - The rotation angle is updated every frame to create a spinning effect.
   - **Justification**: Rotation adds visual interest and makes the stars feel more dynamic.

### 6. **Star Regeneration**
   - When a star moves off the screen, it is replaced with a new star at a random position.
   - **Justification**: This ensures the starfield remains full and visually consistent.

---

## Code Structure

### Key Functions

1. **`new_star()`**:
   - Generates a new star with random coordinates, Z-distance, brightness, and rotation angle.

2. **`move_and_check(star)`**:
   - Updates the star's position, brightness, and rotation angle.
   - Checks if the star has moved off the screen and regenerates it if necessary.

3. **`draw_star(star)`**:
   - Draws a rotating 6-pointed star on the screen using `pygame.draw.polygon`.
   - Applies brightness to the base color.

4. **`apply_brightness(color, brightness)`**:
   - Scales the base color by the brightness value.
