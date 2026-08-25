import Svg, { G, Path } from "react-native-svg";

type Props = {
  size?: number;
  color?: string;
};

/** Figma icon 2016:181 — outer box 10.34 (scaled ×5/3 ≈ 17). */
export function CopyIcon({ size = 17, color = "#FFFFFF" }: Props) {
  return (
    <Svg width={size} height={size} viewBox="0 0 10.3385 10.3385" fill="none">
      <G>
        <Path
          d="M8.61539 3.44615H4.30769C3.83188 3.44615 3.44615 3.83187 3.44615 4.30769V8.61538C3.44615 9.09119 3.83188 9.47692 4.30769 9.47692H8.61539C9.0912 9.47692 9.47692 9.09119 9.47692 8.61538V4.30769C9.47692 3.83187 9.0912 3.44615 8.61539 3.44615Z"
          stroke={color}
          strokeWidth={0.861539}
          strokeLinecap="round"
          strokeLinejoin="round"
        />
        <Path
          d="M1.72308 6.8923C1.24923 6.8923 0.861537 6.50461 0.861537 6.03076V1.72307C0.861537 1.24922 1.24923 0.861531 1.72308 0.861531H6.03077C6.50462 0.861531 6.89231 1.24922 6.89231 1.72307"
          stroke={color}
          strokeWidth={0.861539}
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </G>
    </Svg>
  );
}
