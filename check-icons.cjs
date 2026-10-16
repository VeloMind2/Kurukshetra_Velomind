const fs = require('fs');
const path = require('path');
const lucide = require('lucide-react');

function checkDir(dir) {
  const files = fs.readdirSync(dir);
  for (const f of files) {
    const full = path.join(dir, f);
    if (fs.statSync(full).isDirectory()) {
      checkDir(full);
    } else if (f.endsWith('.tsx') || f.endsWith('.ts')) {
      const content = fs.readFileSync(full, 'utf8');
      const matches = content.matchAll(/import\s*\{([^}]*)\}\s*from\s*['"]lucide-react['"]/g);
      for (const match of matches) {
        const names = match[1].split(',').map(n => n.trim()).filter(Boolean);
        for (const name of names) {
          const cleanName = name.replace(/^type\s+/, '').trim();
          if (!cleanName) continue;
          if (!lucide[cleanName]) {
            console.error('REAL MISSING ICON IN ' + f + ': "' + cleanName + '"');
          }
        }
      }
    }
  }
}

checkDir('./src');
console.log('Icon validation finished.');
