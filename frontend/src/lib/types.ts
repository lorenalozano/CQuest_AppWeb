export interface User {
  id: number;
  username: string;
  email: string;
  xp: number;
  current_world: number;
}

export interface AuthToken {
  access_token: string;
  token_type: string;
  user: User;
}

export interface Lesson {
  id: number;
  world_id: number;
  order: number;
  title: string;
  description: string;
  theory: string;
  starter_code: string;
  expected_output: string;
  hint: string;
  xp_reward: number;
  is_final_project: boolean;
}

export interface World {
  id: number;
  number: number;
  title: string;
  description: string;
  icon: string;
  color: string;
  lessons: Lesson[];
}

export interface UserProgress {
  id: number;
  user_id: number;
  lesson_id: number;
  completed: boolean;
  attempts: number;
  completed_at: string | null;
}

export interface CodeRunResult {
  output: string;
  error: string;
  success: boolean;
  passed: boolean;
  execution_time_ms: number;
}

export interface Badge {
  badge_id: string;
  earned_at: string;
}

export interface ProgressSummary {
  total_lessons: number;
  completed_lessons: number;
  xp: number;
  badges: Badge[];
  worlds_progress: {
    world_number: number;
    world_title: string;
    total: number;
    completed: number;
    unlocked: boolean;
  }[];
}
