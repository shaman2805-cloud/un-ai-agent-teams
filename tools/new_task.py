#!/usr/bin/env python3
"""Create a local, offline task card. Does not call AI services."""
import argparse
import json
from pathlib import Path
from uuid import uuid4


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--team', required=True, choices=['development', 'youtube'])
    parser.add_argument('--project', required=True)
    parser.add_argument('--goal', required=True)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    if not args.project.strip() or not args.goal.strip():
        parser.error('project and goal must not be blank')
    task = {
        'id': str(uuid4()), 'team': args.team,
        'project': args.project.strip(), 'goal': args.goal.strip(),
        'status': 'queued', 'inputs': [], 'dependencies': [],
        'acceptance_criteria': [],
        'limits': {'max_retry_attempts_per_defect': 2, 'money_budget': None, 'currency': None},
        'result': None,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    try:
        with args.output.open('x', encoding='utf-8') as handle:
            json.dump(task, handle, ensure_ascii=False, indent=2)
            handle.write('\n')
    except FileExistsError:
        parser.error('output already exists; choose a new path')
    print(args.output)


if __name__ == '__main__':
    main()
