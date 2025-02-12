---
title: Research
layout: landing
description: Publications and Projects
image: assets/images/pic07.jpg
nav-menu: true
---

<!-- Main -->
<div id="main">


<section id="two">
	<div class="inner">
		<header class="major">
			<h2>Preprints</h2>
		</header>
		<ul class="alt">
			{% for pub in site.data.preprints %}
			<li>{{ pub.authors | join: ', ' }} ({{ pub.year }}) ''{{ pub.title }},'' <a href="{{ pub.link }}">{{ pub.pub_by }}</a>.</li>
			{% endfor %}
		</ul>
	</div>
</section>

<!-- Three -->
<section id="three" class="spotlights">
	<section>
		<a href="profile.html" class="image">
			<img src="{{ '/assets/images/pic08.jpg' | relative_url }}" alt="Work in Progress" />
		</a>
		<div class="content">
			<div class="inner">
				<header class="major">
					<h3>Work in progress</h3>
				</header>
				<div>
					<ul class="alt">
						{% for pub in site.data.working %}
							<li>{{ pub.title }} (related with {{ pub.field | join: ', ' }}).</li>
						{% endfor %}
					</ul>
				</div>
			</div>
		</div>
	</section>
</section>


<section id="four" class="spotlights">
	<section>
		<div class="image">
            <div style="height: 100%; background-color: #f6f6f6; display: flex; justify-content: center; align-items: center;">
                <h1 style="color: #242943; font-size: 2em;">Publications</h1>
            </div>
        </div>
		<div class="content">
		<header class="major">
			<h2>Publications</h2>
		</header>
			<div class="inner">
				<ul class="alt">
					{% for pub in site.data.publications %}
						<li>{{ pub.authors | join: ', ' }} ({{ pub.year }}) ''{{ pub.title }},'' <em><a href="{{ pub.link }}">{{ pub.journal }}</a></em>, {{pub.volume}}.</li>
					{% endfor %}
				</ul>
			</div>
		</div>
	</section>
	<section>
		<a href="generic.html" class="image">
			<img src="{% link assets/images/pic09.jpg %}" alt="" data-position="top center" />
		</a>
		<div class="content">
			<div class="inner">
				<header class="major">
					<h3>Rhoncus magna</h3>
				</header>
				<p>Nullam et orci eu lorem consequat tincidunt vivamus et sagittis magna sed nunc rhoncus condimentum sem. In efficitur ligula tate urna. Maecenas massa sed magna lacinia magna pellentesque lorem ipsum dolor. Nullam et orci eu lorem consequat tincidunt. Vivamus et sagittis tempus.</p>
				<ul class="actions">
					<li><a href="generic.html" class="button">Learn more</a></li>
				</ul>
			</div>
		</div>
	</section>
	<section>
		<a href="generic.html" class="image">
			<img src="{% link assets/images/pic10.jpg %}" alt="" data-position="25% 25%" />
		</a>
		<div class="content">
			<div class="inner">
				<header class="major">
					<h3>Sed nunc ligula</h3>
				</header>
				<p>Nullam et orci eu lorem consequat tincidunt vivamus et sagittis magna sed nunc rhoncus condimentum sem. In efficitur ligula tate urna. Maecenas massa sed magna lacinia magna pellentesque lorem ipsum dolor. Nullam et orci eu lorem consequat tincidunt. Vivamus et sagittis tempus.</p>
				<ul class="actions">
					<li><a href="generic.html" class="button">Learn more</a></li>
				</ul>
			</div>
		</div>
	</section>
</section>

</div>
