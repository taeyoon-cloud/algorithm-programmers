SELECT board.title, board.board_id, reply.reply_id, reply.writer_id,
reply.contents, date_format(reply.created_date, "%Y-%m-%d") as created_date
from used_goods_board as board join used_goods_reply as reply
on board.board_id = reply.board_id
where date_format(board.created_date, "%Y%m") = '202210'
order by reply.created_date, board.title


-- SELECT
--     b.TITLE AS "게시글 제목",
--     b.BOARD_ID AS "게시글 ID",
--     r.REPLY_ID AS "댓글 ID",
--     r.WRITER_ID AS "댓글 작성자 ID",
--     r.CONTENTS AS "댓글 내용",
--     date_format(r.CREATED_DATE, '%Y-%m-%d') AS "댓글 작성일"
-- FROM
--     USED_GOODS_BOARD b
--     JOIN USED_GOODS_REPLY r ON b.BOARD_ID = r.BOARD_ID
-- WHERE
--     date_format(b.CREATED_DATE,'%Y-%m-%d')  >= '2022-10-01'
--     AND date_format(b.CREATED_DATE, '%Y-%m-%d') < '2022-11-01'
-- ORDER BY
--     r.CREATED_DATE ASC,
--     b.TITLE ASC;
