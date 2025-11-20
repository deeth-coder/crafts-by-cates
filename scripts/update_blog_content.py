import json
import os

# Define the new content mapping
# Keys match the 'slug' in blog.json
new_contents = {
    "how-to-block-crochet": """Blocking is often called the “magic step” that transforms crochet from good to great. While some makers skip it, experts and seasoned Reddit users insist that blocking is essential—it settles stitches, evens edges, and brings polish to your work. There are three tried-and-true methods to explore: wet blocking (soaking your piece, pinning it to shape, and letting it dry), steam blocking (using a steamer for gentle shaping without soaking), and spray blocking (spritzing with water and leaving to dry). Each suits different fibers and goals—wool can benefit most from wet blocking, while blends and acrylics often appreciate the lighter touch of spraying or steaming. Makers recommend swatching and blocking your sample first, so you know how your yarn reacts. Ultimately, blocking isn’t just a technicality; it’s a celebration—the final step that elevates “homemade” into a truly “handmade” work of art.

Blocking can also prolong the life and beauty of your handmade garments. It locks in shape, enhances intricate lacework, and corrects minor inconsistencies that naturally occur as you work. A well-blocked project is easier to seam, fits true to size, and appears far more professional. For natural fibers like cotton, linen, and superwash wool, blocking can also soften the fabric and improve drape dramatically. Be aware, though, that each yarn reacts a bit differently: bamboo and superwash wool, for example, may grow more than expected, reminding us of the importance of testing on a swatch.

Beyond technique, blocking fosters mindfulness in the making process. It encourages you to slow down and honor your work at every step, building patience and confidence. Community tips—from dedicated Reddit threads to savvy designers—suggest using tools like foam blocking mats, rust-resistant T-pins, and gentle wool wash. Many crocheters even advocate adding a bit of fabric softener to water for softness and scent! Whether you’re prepping a garment for gifting, selling, or simply wearing, blocking sets your craft apart, marking it as a piece made with true care and intention.""",

    "5-must-try-stitches": """Modern crochet blankets are all about texture, warmth, and personality. Reddit crafters and designers agree: today’s must-try stitches go far beyond the basics, offering stunning dimension and coziness. The Alpine Stitch, Moss Stitch (aka Linen or Granite Stitch), Waffle Stitch, Puff Stitch, and Shell Stitch each bring unique structure—from deep, squishy warmth to elegant, airy drape. Experts suggest picking a stitch that matches your style (think: bold, geometric lines or soft, undulating waves) and experimenting with yarn weight for dramatic effect. These stitches aren’t just visually irresistible—they’re also deeply satisfying to create, making every row a small joy and every finished blanket a modern heirloom.

Choosing your stitch is all about balancing design and purpose. The waffle and puff stitches are perfect for winter throws, as their plush, layered texture traps warmth and feels inviting on cold nights. Moss and shell stitches bring a lighter, modern flair—ideal for summer blankets or elegant decorative throws. When picking yarn, consider chunkier wool for dimension or finer cotton for drape and definition. Seasoned crocheters recommend mixing stitches for personalized style: a blanket panelled with blocks of different texture adds visual interest while keeping the process exciting.

Another insight is the importance of finishing touches. Adding borders—like single crochet for a clean look or picot for a touch of whimsy—frames your work elegantly. Many blanket makers love experimenting with colorwork in these modern stitches; alternating colors brings out the geometry of Alpine and Mosaic stitches, giving each blanket a unique identity. The best part? Each stitch, with its own rhythm and challenges, makes the act of crocheting the blanket as joyful as snuggling under it—helping you to savor the process as much as the result.""",

    "fireside-cardigan-diary": """Documenting your cardigan journey makes the experience twice as rewarding. The process usually begins with dreamy inspiration—often found on Instagram or through beloved bloggers—and quickly moves to hands-on experimentation with yarn, needles, and swatches. From selecting the perfect merino wool (for plush warmth and drape) to sketching out fit and silhouette, every step becomes a part of the story. Knitters share their triumphs and struggles: adjusting the pattern for the right sleeve length, finally getting button bands to lay flat, and mastering the mattress stitch for seamless joining. The final bind-off is a celebration—not just of the finished Fireside Cardigan, but the creativity, resilience, and skill it represents. Sharing your project on social media or your blog invites others to follow, learn, and cheer you on throughout the journey.

Each phase of the project diary reveals invaluable lessons. Swatching and blocking, for example, often expose surprises about yarn behavior—will that merino stretch, or will the colorwork bloom? Troubleshooting along the way is common, from redoing cuffs to experimenting with different joining techniques. Many makers add notes about shaping choices, or pattern modifications to accommodate fit—making the finished garment truly their own. There’s genuine camaraderie in sharing the pitfalls and “aha!” moments with the community.

The final garment holds memories of quiet evenings knitting, bursts of creative energy, and the satisfaction of seeing a vision brought to life. Wearing the cardigan for the first time, or gifting it to a loved one, embodies the warmth and intention poured into every stitch. As you reflect on the diary, it becomes clear that the Fireside Cardigan isn’t just a piece of clothing—it’s proof of growth, skill, and a story written stitch by stitch. A project diary connects every maker to the broader community, inspiring others to take their first step and celebrate each finishline along the way.""",

    "slow-fashion-101": """Choosing slow fashion is a radical act of creativity and self-respect in a world obsessed with speed and disposability. Makers and bloggers emphasize how sewing and knitting their own wardrobes deepens their relationship with clothing—every seam tells a story, every piece lasts, and every fiber reflects conscious choice. Reddit discussions and expert analysis show the slow fashion movement is rapidly growing in 2025, as shoppers tire of micro-trends and look for sustainability, ethical labor, and timeless design. Creating by hand isn’t about thrift—it’s about intention, celebrating quality over quantity, and building a wardrobe (and community) that lasts. In a climate of fast fashion burnout, handmade is more than a trend: it’s a mindset shift that values what we wear and who makes it.

One compelling facet is the environmental impact. Slow fashion prioritizes natural fibers—organic cotton, linen, and hemp—reducing carbon footprint and microplastic pollution compared to synthetics. Brands increasingly tell stories about their garments, highlighting artisans, production processes, and even offering repair kits for lasting use. In this movement, intentional purchases replace impulse buys, leading to capsule wardrobes built on versatility and longevity.

Equally important is the personal transformation. Many makers report feeling more fulfilled and empowered, knowing exactly who made their clothes and how they were made. Social media amplifies this mindset: influencers now showcase handknit sweaters and thrifted finds instead of endless “hauls.” In 2025, thrift and resale platforms are booming, linking ethical shopping and personal story. Ultimately, handmade slow fashion invites us to buy less, choose well, cherish more—and see every garment as an expression of personal and global values.""",

    "garment-sewing-guide": """Getting started in sewing opens up a world of possibility—and the online community, especially on Reddit, is eager to help. Experts and enthusiasts encourage beginners to start simple: choose forgiving fabrics like cotton lawn or linen, and pick projects such as elastic-waist skirts or pull-on shorts that let you practice basic seams and fit. Skipping alterations at first, focusing on following patterns step-by-step, and practicing with inexpensive fabric can build confidence. Other classic advice: always pre-wash your fabric, learn how to press as you go, and don’t be afraid of making mistakes—they’re part of the process! The right tools (good scissors, a sharp seam ripper, and quality pins) make a world of difference. By starting slow and celebrating each project, you’ll be on your way to a custom wardrobe in no time.

Redditors consistently suggest mock garments—using bedsheets or muslin—to test pattern fit and technique before cutting into “real” fabric. Patterns labeled “easy” or “for beginners” are best, and buying indie patterns with video sewalongs can make learning less intimidating. The wisdom is universal: you’ll mess up and that’s okay, because each mistake is a lesson. Many beginners start with a pillowcase, simple shirt, or pajamas to learn the basics: sewing straight seams, practicing hems, and learning to finish edges.

As confidence grows, so does ambition. Try one “difficult” thing per project (like a zipper in a pillowcase or a buttonhole on a skirt) to stretch your skills without overwhelm. Always wash and press your fabric, learn your measurements, and don’t skip the step of pressing between each stage. The journey is about growth—each project is a stepping stone, and patience is your best ally. Embrace trial-and-error, celebrate every win, and before long, you’ll be wearing something that’s truly your own"""
}

blog_file = 'app/content/blog.json'

def update_blog():
    if not os.path.exists(blog_file):
        print(f"Error: {blog_file} not found.")
        return

    with open(blog_file, 'r') as f:
        posts = json.load(f)

    updated_count = 0
    for post in posts:
        slug = post.get('slug')
        if slug in new_contents:
            # Ensure content is clean string with newlines
            post['content'] = new_contents[slug].strip()
            updated_count += 1
            print(f"Updated content for: {post['title']}")
        else:
            print(f"Skipping (no new content found): {post.get('title')}")

    with open(blog_file, 'w') as f:
        json.dump(posts, f, indent=2)
    
    print(f"\nSuccessfully updated {updated_count} blog posts.")

if __name__ == "__main__":
    update_blog()

