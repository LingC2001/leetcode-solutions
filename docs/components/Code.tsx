import fs from 'fs';
import path from 'path';
import { CodeBlock, Pre } from 'fumadocs-ui/components/codeblock';
import { codeToHtml } from 'shiki';

type Language = 'python' | 'cpp' | 'java' | 'go';

interface CodeProps {
  problemNumber: number;
  difficulty: 'easy' | 'medium' | 'hard';
  lang: Language;
  filename?: string;
}

const languageExtensionMap: Record<Language, string> = {
  python: 'py',
  cpp: 'cpp',
  java: 'java',
  go: 'go',
};

const languageLabelMap: Record<Language, string> = {
  python: 'Python',
  cpp: 'C++',
  java: 'Java',
  go: 'Go',
};

export default async function Code({
  problemNumber,
  difficulty,
  lang,
  filename,
}: CodeProps) {
  const difficultyMap = {
    easy: '1-easy',
    medium: '2-medium',
    hard: '3-hard',
  };

  const difficultyFolder = difficultyMap[difficulty];
  const fileExtension = languageExtensionMap[lang];

  const problemsDir = path.join(
    process.cwd(),
    '..',
    'problems',
    difficultyFolder
  );

  const folders = fs.readdirSync(problemsDir);
  const problemFolder = folders.find((folder) =>
    folder.startsWith(`${problemNumber}-`)
  );

  if (!problemFolder) {
    return <div className="text-red-500">Problem folder not found</div>;
  }

  const codeFileName = filename
    ? `${filename}.${fileExtension}`
    : `solution.${fileExtension}`;

  const codePath = path.join(problemsDir, problemFolder, codeFileName);

  if (!fs.existsSync(codePath)) {
    return (
      <div className="text-red-500">
        Code file not found: {codeFileName}
      </div>
    );
  }

  const code = fs.readFileSync(codePath, 'utf-8').trim();

  const html = await codeToHtml(code, {
    lang,
    theme: 'github-dark',
  });

  return (
    <CodeBlock>
      <Pre lang={lang} dangerouslySetInnerHTML={{ __html: html }} />
    </CodeBlock>
  );
}
