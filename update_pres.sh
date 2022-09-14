#abort script on error
# 3,7,4,5,8,9,10,2,1,6
set -e

rm -r Integralrechnung/ || echo "kein dir"
echo "save sections..."
# manim --save_sections -ql scenes.py
manim --save_sections -qh scenes.py
echo "export.."
# manedit --project_name tmp_output  --quick_present_export media/videos/scenes/480p15/sections/intro.json --quick_present_export media/videos/scenes/480p15/sections/inhaltsverzeichnis.json --quick_present_export media/videos/scenes/480p15/sections/praxisbeispiel.json --quick_present_export media/videos/scenes/480p15/sections/konstante_funk.json --quick_present_export media/videos/scenes/480p15/sections/lineare_funk_m_versch.json --quick_present_export media/videos/scenes/480p15/sections/quadratische_funktion.json --quick_present_export media/videos/scenes/480p15/sections/quadratische_funktion_n_rechtecke.json --quick_present_export media/videos/scenes/480p15/sections/zusammenhang.json --quick_present_export media/videos/scenes/480p15/sections/flaeche_beliebiges_intervall.json --quick_present_export media/videos/scenes/480p15/sections/bergriffsdefinitionen.json --quick_present_export media/videos/scenes/480p15/sections/loesen_praxisbeispiel.json --quick_present_export media/videos/scenes/480p15/sections/quellen.json
manedit --project_name Integralrechnung  --quick_present_export media/videos/scenes/1080p60/sections/intro.json --quick_present_export media/videos/scenes/1080p60/sections/inhaltsverzeichnis.json --quick_present_export media/videos/scenes/1080p60/sections/praxisbeispiel.json --quick_present_export media/videos/scenes/1080p60/sections/konstante_funk.json --quick_present_export media/videos/scenes/1080p60/sections/lineare_funk_m_versch.json --quick_present_export media/videos/scenes/1080p60/sections/quadratische_funktion.json --quick_present_export media/videos/scenes/1080p60/sections/quadratische_funktion_n_rechtecke.json --quick_present_export media/videos/scenes/1080p60/sections/zusammenhang.json --quick_present_export media/videos/scenes/1080p60/sections/flaeche_beliebiges_intervall.json --quick_present_export media/videos/scenes/1080p60/sections/bergriffsdefinitionen.json --quick_present_export media/videos/scenes/1080p60/sections/loesen_praxisbeispiel.json --quick_present_export media/videos/scenes/1080p60/sections/quellen.json

# echo "webserver starten.."
# python3 -m http.server --directory tmp_output

rm -r fachreferat_integralrechnung/*
cp -r Integralrechnung/* fachreferat_integralrechnung/
cd fachreferat_integralrechnung/
git add -A
git commit -m "update"
git push
