import React, { useEffect } from "react";
import { useParams, useLocation, useNavigate } from "react-router-dom";
import PrimitivePageLayout from "@layouts/PrimitivePageLayout";
import PRIMITIVES from "@data/primitivesData";

type Props = { id?: string };

const PrimitivePage: React.FC<Props> = ({ id: propId }) => {
  const params = useParams<{ id?: string; primitive?: string }>();
  const location = useLocation();
  const id = propId || params.id || params.primitive;

  const overrides = (location.state && (location.state as { overrides?: Record<string, unknown> }).overrides) || {};

  const data = id ? PRIMITIVES[id] : undefined;
  const navigate = useNavigate();

  useEffect(() => {
    if (!data) {
      navigate("/404", { replace: true });
    }
  }, [data, navigate]);

  if (!data) return null;

  const merged = { ...data, ...overrides };

  return <PrimitivePageLayout data={merged} />;
};

export default PrimitivePage;
