---
layout: page
title: 上級マクロ経済学II
description: 甲南大学/経済学部
image: 
nav-menu: false
show_tile: false
banner_style: style2
---

<!-- Main -->
<div id="main" class="alt">

<!-- One -->
<section id="one">
	<div class="inner">

<!-- Content -->
<h2>概要</h2>
<blockquote>
マクロ経済学で扱うデータについて概観する。
また、pythonを用いて実際にマクロ経済データを分析することを行う。
講義では回帰分析をもとに、生産性の推定やマクロデータの予測などを取り扱う。
さらに、近年盛んに利用されるようになっている、数値計算の基礎についても解説を行う。
</blockquote>

<hr class="major" />

<h3>講義資料</h3>
<div class="table-wrapper">
	<table>
		<thead>
			<tr>
				<th>コンテンツ</th>
				<th>アップデート日</th>
				<th>ダウンロードリンク</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td>第1回資料</td>
				<td>2026/8/15</td>
				<td><a href="{{ site.baseurl }}/assets/html/teaching/advanced_macroeconomicsII/handout1.html" class="button icon fa-file-o">file</a></td>
			</tr>
		</tbody>
	</table>
</div>


<h3>補足資料</h3>
<div class="table-wrapper">
	<table>
		<thead>
			<tr>
				<th>コンテンツ</th>
				<th>アップデート日</th>
				<th>ダウンロードリンク</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td>微分と積分</td>
				<td>2025/9/13</td>
				<td><a href="{{ site.baseurl }}/assets/html/teaching/advanced_macroeconomicsII/main_math.html" class="button icon fa-file-o">file</a></td>
			</tr>
			<tr>
				<td>統計学の概論</td>
				<td>2025/9/13</td>
				<td><a href="{{ site.baseurl }}/assets/html/teaching/advanced_macroeconomicsII/main_statistics.html" class="button icon fa-file-o">file</a></td>
			</tr>
		</tbody>
	</table>
</div>


<hr class="major" />

<div class="row">
	<div class="12u$ 12u$(small)">
		<h3>講義における3つのキーポイント</h3>
	</div>
	
	<div class="4u 12u$(small)">
		<h3>経済成長</h3>
		<p>ソローモデルをスタート地点として、種々の長期的な経済の動態を特徴づけるモデルを概観します。特に、長期的な経済成長を成し遂げるために必要な要因として、いくつかの理論的な経路が考えられることを示します。</p>
	</div>
	<div class="4u 12u$(small)">
		<h3>景気循環</h3>
		<p>経済には2〜4年程度で好況と不況を繰り返す、景気循環と呼ばれる波が存在します。マクロ経済学では、長期的な視座のみでなく、この景気循環についての分析も行われます。本講義では、景気循環が確率的なショックから発生するものとして捉えることを理解することを目指します。また、いくつかの比較的新しい分析において、どのような問題が議論されているかを簡単に紹介します。</p>
	</div>
	<div class="4u$ 12u$(medium)">
		<h3>理論と実証のインタラクション</h3>
		<p>理論モデルを数式として理解するだけではなく、現実の一部を切り取ったベンチマークとして整理することを目指します。理論的に得られる結論と、実証的に観測されている事実を比較・整理します。</p>
	</div>
</div>

<hr class="major" />

<div class="row">
	<div class="6u$ 12u$(small)" style="float: none; margin: 0 auto;">
		<header>
			<h3>質問フォーム</h3>
		</header>
		<!--質問-->
		<br>
		<form method="post" action="https://YoshitakaOgisu.pythonanywhere.com/submit_reaction"> 
			<!-- 講義識別子 -->
			<input type="hidden" name="course_id" value="adv_macroII">
			<!--コンテンツ識別子-->
			<input type="hidden" name="content_type" value="qa">
			<div class="row">
				<div class="4u 12u$(small)">
					<h4 align="center">名前（任意）</h4>
				</div>
				<div class="8u$ 12u$(small)">
					<input type="text" name="student_name" id="student_name" placeholder="名無しさん"/>
				</div>
			</div>
			<br>
			<!-- 質問内容 -->
			<h4>質問</h4>
			<textarea name="adv_macroII_question" id="adv_macroII_question" 
					placeholder="質問を入力してください" rows="6" required></textarea>
			<br>
			<div class="12u$" align="center">
				<ul class="actions">
					<li><input type="submit" value="質問送信" class="special" /></li>
					<li><input type="reset" value="リセット" /></li>
				</ul>
			</div>
		</form>
	</div>
</div>


<hr class="major" />


<section>
  <div class="inner" align="center">
	<ul class="actions">
	  <li><a href="{{ site.baseurl }}/03-teaching.html" class="button">Go back Teaching</a></li>
	</ul>
  </div>
</section>

<section>
  <div class="inner" align="center">
	<ul class="actions">
	  <li><a href="{{ site.baseurl }}/index.html" class="button">Home</a></li>
	  <li><a href="#banner" class="button special scroll">Page top</a></li>
	</ul>
  </div>
</section>

<!--End Contents-->
	</div>
</section>

</div>
