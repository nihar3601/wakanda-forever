def on_on_overlap(sprite, otherSprite):
    info.change_score_by(1)
    Namor.set_position(148, 2)
sprites.on_overlap(SpriteKind.guard, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    info.change_life_by(-1)
    Namor.set_position(148, 2)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap2)

def on_on_score():
    Namor.destroy()
    scene.set_background_image(assets.image("""
        boston-bridge
    """))
    effects.confetti.start_screen_effect()
    Shuri.say_text("Wakanda Forever!!!")
info.on_score(20, on_on_score)

Namor: Sprite = None
Shuri: Sprite = None
game.show_long_text("When game begins, press the ARROW KEYS to move Shuri, Okoye and Riri. If Namor catches you, you will lose points! ",
    DialogLayout.FULL)
scene.set_background_image(assets.image("""
    wakanda
"""))
Shuri = sprites.create(assets.image("""
    shuri
"""), SpriteKind.player)
controller.move_sprite(Shuri)
Shuri.set_stay_in_screen(True)
Namor = sprites.create(assets.image("""
    namor
"""), SpriteKind.enemy)
Namor.set_position(148, 2)
Namor.follow(Shuri, 30)
Riri = sprites.create(assets.image("""
    riri
"""), SpriteKind.guard)
Okoye = sprites.create(assets.image("""
    okoye
"""), SpriteKind.guard)
controller.move_sprite(Riri, 34, -53)
controller.move_sprite(Okoye, -68, -58)
Okoye.set_stay_in_screen(True)
Riri.set_stay_in_screen(True)