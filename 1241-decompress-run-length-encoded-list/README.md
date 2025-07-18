<h2><a href="https://leetcode.com/problems/decompress-run-length-encoded-list">1241. Decompress Run-Length Encoded List</a></h2><h3>Easy</h3><hr><p>We are given a list <code>nums</code> of integers representing a list compressed with run-length encoding.</p>

<p>Consider each adjacent pair of elements <code>[freq, val] = [nums[2*i], nums[2*i+1]]</code> (with <code>i >= 0</code>).  For each such pair, there are <code>freq</code> elements with value <code>val</code> concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.</p>

<p>Return the decompressed list.</p>

<p> </p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [2,4,4,4]
<strong>Explanation:</strong> The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,2,3]
<strong>Output:</strong> [1,3,3]
</pre>

<p> </p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 <= nums.length <= 100</code></li>
	<li><code>nums.length % 2 == 0</code></li>
	<li><code><font face="monospace">1 <= nums[i] <= 100</font></code></li>
</ul>
