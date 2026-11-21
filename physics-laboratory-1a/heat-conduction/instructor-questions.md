# Questions for the instructor — heat conduction

Todo 5b. Drafted 2026-11-04, sent by the user 2026-11-04.
Dropped question 3 (where the heat is produced), 2026-11-04: T p. 3 settles it. P_in = VI comes from a resistor and enters at one end of the tube ("בקצה אחד נכנס P_in"). B's "הצינור משמש כנגד" is loose wording.

---

שלום,

יש לי שאלה לגבי הרקע התיאורטי בניסוי הולכת חום.

בנוסחה (3) מופיע P(x)/A = −κ·dT/dx, ובנוסחה (4) מופיע T(x) = T(0) + (P/κA)·x עם סימן פלוס. לפי נוסחה (3), אם x נמדד מהקצה החם לכיוון מאגר המים, הטמפרטורה יורדת לאורך המוט והשיפוע צריך להיות −P/(κA).

1. מאיזה קצה של המוט נמדד x = 0 באיור 4 בתדריך: מצד החימום או מצד מאגר המים?
2. האם הסימן בנוסחה (4) צריך להיות מינוס, או שכיוון x מוגדר כך שהפלוס נכון?

תודה!

---

## Cover "חלק" field (added 2026-11-04, sent 2026-11-04)

בדף השער יש שדה "חלק". מה צריך לכתוב בו בדו"ח של הולכת חום? בניסוי יש שלושה חלקים (א, ב, ג), וכולם נכללים בדו"ח אחד.

---

## Theory-background wording (todos 9c, 9d, 9e) — drafted 2026-11-04, sent, answered 2026-11-05 (see below)

שלום תמיר,

אני מעתיק את הרקע התיאורטי של ניסוי הולכת חום מקובץ הפורמט שבמודל, ומצאתי בו שלושה מקומות שנראים לי כטעויות. האם לתקן אותם בדו"ח, או להשאיר את הטקסט כפי שהוא?

1. "מוחזק במגע עם אובייקט חם מצד אחד ואובייקט חם מצד שני": האם בצד השני צריך להיות "קר"?
2. בביטוי P ∝ (T₂ − T₁)/L האות L מסמנת אורך, אבל בנוסחה (1) L הוא קבוע לורנץ. האם להחליף את האורך כאן ב-L₀ (אורך הגליל, כמו בנוסחה (2))?
3. "הביטוי בנוסחה מס׳ (3) לאחר תיקון מסדר ראשון יהיה P(x) = P_avg": ההספק המתוקן מחליף את P בנוסחה (4), ובקובץ הרקע התיאורטי המלא כתוב "הקשר שלמעלה". האם ההפניה צריכה להיות לנוסחה (4)?

תודה!

---

## Answers from Tamir (received 2026-11-05, pasted by the user as screenshots)

Note: the sent version of the sign email still contained question 3 (does the whole tube act as the resistor, or only the small part at x = 0?), although the draft above dropped it.

**Sign email (todo 5b / 9f):**
1. x = 0 is at the heating side, where the resistor is.
2. Formula (4) should have a minus sign. "You're right."
3. The heat is produced at one end of the tube. (4) is derived assuming steady state, with the same power along the whole rod, so it would not be a problem either way.

**Cover "חלק" field (todo 7b):** he thinks the field belongs to Lab 1a part 2 (next semester), is not sure, will check and reply. Still open.

**Theory wording 9c–9e:** "You don't need to change anything in the background, copy it as is." The staff will fix the theory for next year. On point 3: referring to (3) or (4) is the same thing for the power correction, since (4) is derived from (3).

---

## Error of σ: a and w share D_ch (todo 11c) — drafted 2026-11-05, sent by the user 2026-11-05, waiting

שלום תמיר,

שאלה לגבי חישוב השגיאה במוליכות החשמלית σ בחלק א׳ (נוסחה (2) ברקע התיאורטי).

הרדיוס הפנימי a ועובי הדופן w מחושבים שניהם מקוטר התעלה D_ch שמדדנו: a = D_ch/2 ו-w = (D − D_ch)/2, כאשר D הוא הקוטר החיצוני. לכן השגיאות ב-a וב-w אינן בלתי תלויות, ונוסחה (43) בחוברת עיבוד הנתונים מניחה משתנים בלתי תלויים.

1. האם מספיק לחשב את השגיאה ב-σ לפי נוסחה (43) כאילו a ו-w בלתי תלויים?
2. או שצריך לכתוב את σ כפונקציה של המשתנים שנמדדו ישירות (D_ch ו-D), ולגזור לפיהם?

בנתונים שלנו ההבדל זניח: השגיאה היחסית ב-σ היא 2.22% בדרך הראשונה ו-2.24% בשנייה.

תודה!

איתמר אביגדורי
סטודנט במעבדה לפיזיקה א 1

**Tamir's reply (2026-11-06, pasted by the user 2026-11-09):** "send me the calculation both ways, I think it should give the same result."

### Follow-up email (drafted 2026-11-09, shortened the same day at the user's request, sent by the user 2026-11-09, waiting). Attach emails/sigma-error-tamir.pdf (1 page, built by emails/make_sigma_error.py)

שלום תמיר,

מצורף החישוב בשתי הדרכים. לאחר עיגול שתיהן נותנות σ = (6.70 ± 0.15)·10⁷ S/m. לפני העיגול ההפרש הוא איבר צולב אחד, כי D_ch מופיע גם ב-a וגם ב-w.

האם להשתמש בדו"ח בדרך הראשונה?

תודה,
איתמר

---

## Part ג rates (todo 11f) — drafted 2026-11-09, sent by the user 2026-11-09, waiting

שלום תמיר,

כמה שאלות על חלק ג׳ בהולכת חום:

1. את קצבי הקירור והחימום לחשב מהטמפרטורה הממוצעת של שמונת החיישנים, או מחיישן אחד?
2. החימום אצלנו לא לינארי, השיפוע יורד מ-1.2 ל-0.97 מעלות לדקה לאורך 15 הדקות. לעשות התאמה לינארית על כל המקטע, או רק סביב רגע ההדלקה של הספק?
3. את $\dot T_{exp}$ לקחת מהשיפוע בסוף חלק ב׳ (סביב השורה שבה עשינו את ההתאמה)?

תודה,
איתמר

---

## Sensor position error (todo 11d-4) — sent by the user 2026-11-09, answered

Question: is the 2 mm sensor-position error the final error or the resolution?
**Tamir (2026-11-09):** "זאת השגיאה הסופית לא הרזולוציה." → x error = 2 mm as used; red removed from the plan.

**Tamir's answer on part ג rates (2026-11-09, pasted 2026-11-10):**
1. One sensor, preferably one from the middle of the rod.
2. Fit where the temperature change is linear. Not near the power switch-on (extreme changes there that make it non-linear). Pick a region in the middle of the heating time that looks relatively linear, with enough points. It won't be perfectly linear, but do a linear fit anyway; that is part of the approximations. Deviations from linearity can explain problems in the analysis, if any; the question is how significant they are.
3. Yes: Ṫ_exp where the graph is already almost flat, for a single sensor.

**Cover "חלק" field — Tamir's final answer (2026-11-09, pasted 2026-11-10):** "בדקתי ואתם לא צריכים למלא את השדה שנקרא 'חלק' בדף הפתיחה." → left empty.

**Tamir's reply on the σ error (pasted 2026-11-10):** he gets ((1/D_ch + 1/(D − D_ch))·ΔD_ch)² + (ΔD/(D − D_ch))² for way ב (we have 2/D_ch), says the two ways should then be equivalent ("only the order of calculation differs"), and says g has no error in this experiment. Asks us to check; email him if it doesn't work out.
Check (2026-11-10): a appears squared in (2), so ∂ln σ/∂D_ch = 2/D_ch + 1/(D − D_ch); a numerical derivative of (2) gives 0.40374, ours 0.40374, his 0.23776. With his term the ways still differ (1.945% vs 1.973%, without g). Without Δg both ways round to Δσ = 0.13·10⁷ S/m.

### Reply (drafted 2026-11-10, softened at the user's request 2026-11-13, sent by the user 2026-11-13, waiting)

שלום תמיר,

תודה על הבדיקה! ניסיתי לשחזר את הביטוי שלך, ויצא לי 2/D_ch במקום 1/D_ch, כי a מופיע בריבוע בנוסחה (2) ו-a = D_ch/2. אולי פספסתי משהו?

בכל מקרה, אחרי שהורדתי את השגיאה של g כמו שאמרת, שתי הדרכים נותנות אחרי עיגול את אותה תוצאה, σ = (6.70 ± 0.13)·10⁷ S/m. אז אם זה בסדר מבחינתך, אשתמש בדו"ח בדרך הראשונה.

תודה,
איתמר

---

## New briefing + theory (todo 17) — drafted 2026-11-14, sent by the user 2026-11-14, waiting

שלום תמיר,

ראיתי שבמודל עלו תדריך ורקע תיאורטי חדשים להולכת חום (תשפ"ז, מ-12.11), כלומר אחרי שעשינו את הניסוי ב-2.11. התדריך השתנה מאז שהתחלנו, ועד עכשיו כתבתי את הדו"ח לפי התדריך והרקע התיאורטי הקודמים. יש ביניהם כמה הבדלים שמשנים את החישובים:

1. לפי איזה רקע תיאורטי לכתוב את הדו"ח, הישן או החדש?
2. התדריך החדש מפנה ל"מקור התיאורטי" (חלקים 1–6, נוסחה (16)). איפה אפשר למצוא אותו?
3. בתדריך החדש (סעיף 1.8) כתוב שהצינור של חלק 2 מלא, בלי קדח, כלומר A = πb². אני חישבתי את A כשטח טבעת, לפי קוטר התעלה. מה נכון לצינור שעבדנו איתו? ואם הוא מלא, הרדיוס החיצוני שלו זהה לזה של הצינור מחלק 1?
4. ברקע החדש T בחוק וידמן-פרנץ היא הטמפרטורה הממוצעת של המתכת, ואני השתמשתי בטמפרטורת החדר (24°C, שגיאה של 1K) לפי מה שנאמר במעבדה. מה נכון? אם הממוצעת, הכוונה לממוצע של שמונת החיישנים במדידה שעליה עשיתי את ההתאמה?
5. לגבי Ṫ_exp: אמרת לקחת את השיפוע בסוף חלק 2, ובתדריך החדש (חלק 4) מבקשים התאמה לא לינארית לעקומת הטמפרטורה ונגזרת בזמן מסוים. לפי מה לעבוד?
6. בתדריך החדש חלק 1 הוא בונוס לקבוצות פיזיקה וחלק 4 בונוס לקבוצות הנדסה. אני בפיזיקה, אז אילו חלקים חובה בדו"ח?
7. בחלק 3 בתדריך החדש מבקשים לחשב גם את קיבול החום ואת P_loss, עם שגיאות. צריך להציג אותם בדו"ח?

ההבדלים בסעיפים 3 ו-4 משנים את קבוע לורנץ שיוצא לי בכ-10%, ולכן חשוב לי לדעת לפני שאני ממשיך.

תודה,
איתמר

### Optional follow-up (drafted 2026-11-14) — user decided not to send it (2026-11-14) — after finding the "מקור תיאורטי" on Moodle

שלום תמיר,

מצאתי במודל את "הרחבת רקע תיאורטי", והיא עונה על חלק מהשאלות ששלחתי (Ṫ_exp, קיבול החום ו-P_loss). נשארו כמה:

1. האם לכתוב את הרקע התיאורטי לפי הפורמט החדש שעלה ב-12.11?
2. הצינור בחלק 2 מלא (A = πb²) או חלול?
3. T בחוק וידמן-פרנץ היא הממוצע של שמונת החיישנים בזמן ההתאמה?
4. בנוסחה (14) במקור התיאורטי כתוב C = P_in/(Ṫ_heat + Ṫ_cool), אבל מחיסור נוסחאות (12) ו-(13) יוצא לי Ṫ_heat − Ṫ_cool. מה נכון?
5. השגיאה במיקום החיישנים: 2 מ"מ כמו שאמרת, או לפי הקדח של 1.3 מ"מ שמופיע במקור התיאורטי?

ההגשה ב-16.11, אז אשמח לתשובה כשתוכל.

תודה,
איתמר

**Tamir's reply to the new-briefing email (pasted 2026-11-15):** materials are being updated, but it shouldn't affect us.
1. Keep using the OLD theory background.
2. He'll check (where the theory source is) — moot, found on Moodle.
3. The part-2 rod is SOLID: A = π(d/2)², d = the rod's diameter; the rod measured in part 1 is identical to the one the heat flows through in parts 2–3 (same outer diameter). If redoing the calculations takes much time, talk to him.
4. T = the metal's mean temperature, estimated as ROOM temperature (the measurements ran at different temperatures, so there is no clear way to define the mean): keep 24 °C.
5. Ṫ_exp: the linear fit at the end of part 2 as explained; the briefing's version is more complex than needed.
6. Part 1 became a bonus because instructors don't explain it to all students; we write the full processing of parts 1, 2 and 3.
7. Every calculation must appear in the analysis plan (formulas for quantities and errors), but the results needn't show intermediate numbers like P_loss and its error.
Still unanswered: the σ-error correlation (formulas (7)/(14)).

**Tamir's second reply on the σ error (pasted 2026-11-15):** "you are right, my mistake" (our 2/D_ch, since a is squared in (2)). The correct way is the SECOND way (σ written in terms of the directly measured D_ch and D), even though it is more complex: use it. Tell him if there is a problem.
