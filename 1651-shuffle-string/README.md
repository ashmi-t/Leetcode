<h2><a href="https://leetcode.com/problems/shuffle-string">1651. Shuffle String</a></h2><h3>Easy</h3><hr><p>You are given a string <code>s</code> and an integer array <code>indices</code> of the <strong>same length</strong>. The string <code>s</code> will be shuffled such that the character at the <code>i<sup>th</sup></code> position moves to <code>indices[i]</code> in the shuffled string.</p>

<p>Return <em>the shuffled string</em>.</p>

<p> </p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/07/09/q1.jpg" style="width: 321px; height: 243px;" />
<pre>
<strong>Input:</strong> s = "codeleet", <code>indices</code> = [4,5,6,7,0,2,1,3]
<strong>Output:</strong> "leetcode"
<strong>Explanation:</strong> As shown, "codeleet" becomes "leetcode" after shuffling.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = "abc", <code>indices</code> = [0,1,2]
<strong>Output:</strong> "abc"
<strong>Explanation:</strong> After shuffling, each character remains in its position.
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>s.length == indices.length == n</code></li>
	<li><code>1 <= n <= 100</code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
	<li><code>0 <= indices[i] < n</code></li>
	<li>All values of <code>indices</code> are <strong>unique</strong>.</li>
</ul>
