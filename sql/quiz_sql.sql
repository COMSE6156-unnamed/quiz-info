create table  quiz (
  quiz_id int auto_increment primary key,
  difficulty int
);

create table question (
  question_id int auto_increment primary key,
  right_answer_id int,
  other_choice_id1 int, 
  other_choice_id2 int,
  other_choice_id3 int,
  difficulty int
);

create table quiz_question (
  quiz_id int,
  question_id int
);

create table user_answer (
  user_id int,
  quiz_id int, 
  question_id int,
  choice_id int
);
