document.addEventListener("DOMContentLoaded", async () => {
    const container = document.getElementById("pixi-container");
    if (!container || !window.PIXI) return;

    // ---- Init Pixi App (v8 way) ----
    const app = new PIXI.Application();
    await app.init({
        width: 800,
        height: 400,
        backgroundColor: 0xffffff,
        antialias: true,
    });

    container.appendChild(app.canvas);

    // ---- Helpers ----
    function darken(hex, factor) {
        const r = ((hex >> 16) & 255) * factor;
        const g = ((hex >> 8) & 255) * factor;
        const b = (hex & 255) * factor;
        return (r << 16) | (g << 8) | b;
    }

    function createIsoCube(color) {
        const g = new PIXI.Graphics();

        const size = 40;
        const height = 30;

        // Top
        g.beginFill(color);
        g.drawPolygon([
            0, 0,
            size, -size / 2,
            size * 2, 0,
            size, size / 2,
        ]);
        g.endFill();

        // Left
        g.beginFill(darken(color, 0.8));
        g.drawPolygon([
            0, 0,
            size, size / 2,
            size, size / 2 + height,
            0, height,
        ]);
        g.endFill();

        // Right
        g.beginFill(darken(color, 0.6));
        g.drawPolygon([
            size, size / 2,
            size * 2, 0,
            size * 2, height,
            size, size / 2 + height,
        ]);
        g.endFill();

        return g;
    }

    // ---- Create cubes ----
    const colors = [0xff4444, 0x4488ff, 0xffcc00];
    const cubes = [];

    const spacing = 140;
    const baseX = 100;
    const baseY = 220;

    colors.forEach((color, i) => {
        const cube = createIsoCube(color);
        cube.x = baseX + i * spacing;
        cube.y = baseY;
        app.stage.addChild(cube);
        cubes.push(cube);
    });
    colors.forEach((color, i) => {
        const cube = createIsoCube(color);
        cube.x = baseX + i * spacing;
        cube.y = baseY;
        app.stage.addChild(cube);
        cubes.push(cube);
    });
    
    const chain = new PIXI.Graphics();
    app.stage.addChild(chain);

    function drawChainLinks(a, b) {
        const links = 6;

        for (let i = 1; i < links; i++) {
            const t = i / links;
            const x = a.x + (b.x - a.x) * t + 40;
            const y = a.y + (b.y - a.y) * t + 15;

            chain.beginFill(0x666666);
            chain.drawEllipse(x, y, 6, 3);
            chain.endFill();
        }
    }

    // ---- Endless carousel animation ----
    const duration = 6; // seconds per loop
    let elapsed = 0;

    app.ticker.add((ticker) => {
        elapsed += ticker.deltaMS / 1000;

        cubes.forEach((cube, i) => {
            const t = ((elapsed / duration) + i / cubes.length) % 1;
            cube.x = baseX + t * spacing * cubes.length;

            // seamless wrap
            if (cube.x > baseX + spacing * (cubes.length - 1)) {
                cube.x -= spacing * cubes.length;
            }
        });
        chain.clear();
        for (let i = 0; i < cubes.length; i++) {
            const a = cubes[i];
            const b = cubes[(i + 1) % cubes.length];
            drawChainLinks(a, b);
        }
    });
});
