"""Regenera os .zip de claude-web/ a partir de claude-code/.

Rodar da raiz do repo: python scripts/build-zips.py
Valida cada skill (name = pasta, description <= 1024) e cada zip (barra normal, sem espaço),
que é o formato que o upload do Claude.ai aceita.
"""
import zipfile, os, re, pathlib
root = pathlib.Path("claude-code"); out = pathlib.Path("claude-web"); out.mkdir(exist_ok=True)
for old in out.glob("*.zip"): old.unlink()
for skill in sorted(p.name for p in root.iterdir() if p.is_dir()):
    t = (root/skill/"SKILL.md").read_text(encoding="utf-8")
    name = re.search(r"^name:\s*(\S+)", t, re.M).group(1)
    desc = re.search(r"^description:\s*(.*)$", t, re.M).group(1)
    assert name == skill, (name, skill)
    assert len(desc) <= 1024, (skill, len(desc))
    z = out/f"{skill}.zip"
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for dp, _, fs in os.walk(root/skill):
            for f in sorted(fs):
                full = pathlib.Path(dp)/f
                arc = full.relative_to(root).as_posix()
                zf.write(full, arc)
    names = zipfile.ZipFile(z).namelist()
    bad = [n for n in names if "\\" in n or " " in n or not re.fullmatch(r"[A-Za-z0-9._/\-]+", n)]
    assert not bad, (skill, bad)
    assert f"{skill}/SKILL.md" in names
    print(f"{skill:20s} {len(names):3d} arquivos  {z.stat().st_size/1024:7.0f} KB  desc={len(desc)}")
