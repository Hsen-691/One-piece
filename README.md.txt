# FriesLab Menu

A pirate-themed digital menu for FriesLab: customers add items to a treasure chest, a straw-hat mascot stretches his arm to grab each item, and the order is sent on WhatsApp. After ordering, customers can play a mini-game to earn loyalty points.

Works on phones, tablets and desktop browsers, and can be added to a phone's home screen like an app.

## Features

- **Treasure chest cart.** The chest opens and fills with coins as items are added.
- **Stretchy-arm grab.** Tap **+** and the mascot reaches out, grabs the food and drops it in the chest.
- **13 categories, 83 items** with photos, prices, descriptions and spicy / bestseller / new tags.
- **WhatsApp checkout.** Delivery, dine-in or take-out; the full order is typed into WhatsApp automatically.
- **Loyalty ranks.** Stowaway → Deckhand → Navigator → First Mate → Captain → Pirate King (10 points per $1).
- **Hat Flight mini-game.** Earn extra points after ordering.
- **Responsive layout.** Phone layout on mobile, a three-column layout on desktop.

## Files

| File | What it is |
|---|---|
| `index.html` | The whole menu app (layout, styles and code) |
| `menu-data.js` | Categories and items (names, prices, descriptions, photos) |
| `logo.webp` | FriesLab logo |
| `manifest.json` | Lets customers "Add to Home Screen" |
| `fetch_menu.py` | Refreshes `menu-data.js` from the live frieslab.net menu |

---

## Before you deploy: set the WhatsApp number

Open `index.html`, find this line near the top of the `<script>` section:

```js
const WHATSAPP_NUMBER = '';
```

Put FriesLab's number in international format, **digits only** (no `+`, spaces or dashes). For Lebanon that starts with `961`:

```js
const WHATSAPP_NUMBER = '96170123456';
```

If you leave it empty, WhatsApp still opens with the order typed out, but the customer has to choose the chat themselves.

---

## Deploy on GitHub Pages

GitHub Pages hosts the menu for free at a link like `https://YOUR-USERNAME.github.io/frieslab-menu/`.

### Option A: in the browser (no tools needed)

1. Sign in at [github.com](https://github.com) (create a free account if you don't have one).
2. Click **+** (top right) → **New repository**.
3. Name it `frieslab-menu`, set it to **Public**, and click **Create repository**.
4. On the new repository page, click **uploading an existing file**.
5. Drag in all the files from this folder: `index.html`, `menu-data.js`, `logo.webp`, `manifest.json`, `fetch_menu.py` and `README.md`.
6. Click **Commit changes**.
7. Go to **Settings** → **Pages** (left sidebar).
8. Under **Build and deployment** → **Source**, choose **Deploy from a branch**.
9. Set **Branch** to `main` and the folder to `/ (root)`, then click **Save**.
10. Wait 1–2 minutes and refresh the page. Your link appears at the top:
    `https://YOUR-USERNAME.github.io/frieslab-menu/`

### Option B: with Git on the command line

Create an empty repository named `frieslab-menu` on GitHub first (steps 1–3 above), then run these from inside this folder:

```bash
git init
git add index.html menu-data.js logo.webp manifest.json fetch_menu.py README.md
git commit -m "FriesLab menu"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/frieslab-menu.git
git push -u origin main
```

Then turn on Pages (steps 7–10 above).

---

## Updating the menu after it's live

### Change prices or items by hand

Edit `menu-data.js`. Each item looks like this:

```js
{
 "id": "my-new-burger-1",
 "cat": "a7c9e87b-51b7-4039-b896-e716bc5d5976",
 "name": "THE NEW ONE",
 "price": 12.5,
 "desc": "Angus patty, cheddar, pickles, secret sauce",
 "img": "https://link-to-photo.webp",
 "hot": false,
 "best": false,
 "isNew": true
}
```

- `id`: any unique text.
- `cat`: the `id` of a category from the `"categories"` list at the top of the file.
- `price`: a number, no `$`.
- `hot`, `best`, `isNew`: `true` or `false`; they show the spicy, bestseller and new tags.
- Items are separated by commas, so add a comma after the `}` of the item before yours.

On GitHub you can edit the file in the browser: open `menu-data.js` → click the pencil icon → make your change → **Commit changes**. The live site updates within a minute or two.

### Pull the latest menu from frieslab.net

If the menu changed on frieslab.net, refresh everything automatically (requires [Python](https://www.python.org/downloads/)):

```bash
python fetch_menu.py
```

Then upload the new `menu-data.js` to GitHub.

---

## Run it on your computer

Browsers block some features when you open `index.html` by double-clicking, so start a small local server from this folder:

```bash
python -m http.server 5178
```

Then open http://localhost:5178 in your browser. To jump straight to the mini-game, open http://localhost:5178/#play.

---

## Good to know

- **Photos come from frieslab.net.** If an image is removed or renamed on that site, it breaks here too. To make the menu independent, download the photos into an `images/` folder, upload them with the rest, and change each `img` link to `images/filename.webp`.
- **Loyalty points are stored in each customer's browser.** They reset if a customer clears their browser or switches phones, and they aren't protected against cheating. Real accounts need a backend (for example Supabase or Firebase).
- **No admin panel yet.** Menu changes are made in `menu-data.js` as described above.
- **The mascot is an original character,** not Luffy, because One Piece characters are copyrighted. If FriesLab has licensed artwork, it can replace the `mascotSym` drawing in `index.html`; the stretchy arm starts from the `SHOULDER` point set at the top of the script.
