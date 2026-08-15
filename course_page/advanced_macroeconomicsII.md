---
layout: page
title: 上級マクロ経済学II
description: 甲南大学/経済学部
image: 
nav-menu: false
show_tile: false
banner_style: style3
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
		<h3>Pythonの基本</h3>
		<p>上級マクロ経済学では、Pythonを用いてデータの分析を行います。実際に取り扱う内容はごくごく一部ですが、基本的な文法や動作を学ぶことで、今後コーディングを実践する際に役立つでしょう。講義ではGoogle Colaboratoryを用いて、サンプルコードを実際に動かしながら、基本的な操作を学びます。</p>
	</div>
	<div class="4u 12u$(small)">
		<h3>データハンドリング</h3>
		<p>取得したデータを実際に分析が容易な形にする整形作業は、実はかなり面倒です。ただし、近年ではデータベースの整備が進み、フォーマットの統一などもされるようになってきました。講義を通してデータテーブルを直接変更するのではなく、コードを通してデータテーブルの中の必要なデータを抽出し、自らが分析しやすい形に整形する一連の流れを身につけましょう。</p>
	</div>
	<div class="4u$ 12u$(medium)">
		<h3>統計モデルの基礎</h3>
		<p>講義では最もシンプルな線形回帰や自己回帰モデル（ARモデル）を取り扱うことで、マクロ経済の性質や動態をラフに分析することができるようになることを目指します。講義で扱える内容は多く有りませんが、ここをスタート地点としてそれぞれの関心に沿った次のステップへ進みましょう。</p>
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
