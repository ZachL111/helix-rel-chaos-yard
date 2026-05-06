// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "../src/DomainReview.sol";

contract DomainReviewTest {
    function testDomainReviewLane() public pure {
        DomainReview lens = new DomainReview();
        DomainReview.Item memory item = DomainReview.Item(69, 39, 13, 50);
        require(lens.score(item) == 188, "domain score mismatch");
        require(lens.lane(item) == 2, "domain lane mismatch");
    }
}
